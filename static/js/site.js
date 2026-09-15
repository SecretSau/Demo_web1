"use strict";

const menuToggle = document.querySelector(".menu-toggle");
const navigation = document.querySelector("#main-nav");
function closeMenu() {
  navigation.classList.remove("open");
  menuToggle.setAttribute("aria-expanded", "false");
  menuToggle.setAttribute("aria-label", "Open navigation");
}
menuToggle.addEventListener("click", () => {
  const expanded = menuToggle.getAttribute("aria-expanded") !== "true";
  navigation.classList.toggle("open", expanded);
  menuToggle.setAttribute("aria-expanded", String(expanded));
  menuToggle.setAttribute("aria-label", expanded ? "Close navigation" : "Open navigation");
});
navigation.querySelectorAll("a").forEach(link => link.addEventListener("click", closeMenu));
document.addEventListener("keydown", event => {
  if (event.key === "Escape" && navigation.classList.contains("open")) {
    closeMenu();
    menuToggle.focus();
  }
});
window.matchMedia("(min-width: 681px)").addEventListener("change", closeMenu);

const dialog = document.querySelector("#transfer-dialog");
const accounts = JSON.parse(document.querySelector("#donation-data").textContent);
const fieldDefinitions = [
  ["bank_name", "Bank", "Your bank name"],
  ["account_name", "Account name", "Mission account name"],
  ["account_number", "Account number", "XXXX XXXX XXXX"],
  ["currency", "Currency", "PHP / your currency"],
  ["swift_code", "SWIFT / BIC", "Your bank’s SWIFT code"],
  ["bank_address", "Bank address", "Your bank’s address"],
  ["reference", "Transfer reference", "Donation / your reference"]
];
let currentAccount;
let opener;
let toastTimer;

function toast(message) {
  const el = document.querySelector(".toast");
  clearTimeout(toastTimer);
  el.textContent = message;
  el.classList.add("visible");
  toastTimer = setTimeout(() => el.classList.remove("visible"), 3000);
}

async function copyText(value) {
  try {
    if (!navigator.clipboard || !window.isSecureContext) throw new Error("Clipboard unavailable");
    await navigator.clipboard.writeText(value);
    toast("Copied. Check the recipient in your banking app.");
  } catch {
    // Select text locally when clipboard permission is unavailable.
    const area = document.createElement("textarea");
    area.value = value;
    area.setAttribute("aria-label", "Select and copy these account details");
    area.readOnly = true;
    dialog.append(area);
    area.focus();
    area.select();
    let copied = false;
    try { copied = document.execCommand("copy"); } catch { /* Manual selection remains available. */ }
    if (copied) {
      area.remove();
      toast("Account details copied.");
    } else {
      toast("Press Ctrl+C or long-press to copy the selected details.");
      area.addEventListener("blur", () => area.remove(), {once: true});
    }
  }
}

function fieldsFor(account) {
  return fieldDefinitions.filter(([key]) => {
    if (account.ready) return Boolean(account[key]);
    return key !== "bank_address" && (key !== "swift_code" || account.kind === "international");
  });
}

document.querySelectorAll(".transfer-open").forEach(button => {
  button.addEventListener("click", () => {
    currentAccount = accounts.find(account => account.id === button.dataset.account);
    if (!currentAccount) return;
    opener = button;
    document.querySelector("#dialog-title").textContent = currentAccount.label;
    document.querySelector("#dialog-description").textContent = currentAccount.ready
      ? "Copy these details into your own banking app."
      : "An example of how you’ll give directly through your bank.";
    document.querySelector("#account-pending").hidden = true;
    document.querySelector("#account-ready").hidden = false;
    let badge = document.querySelector(".demo-badge");
    if (!badge) {
      badge = document.createElement("p");
      badge.className = "demo-badge";
      document.querySelector("#account-ready").prepend(badge);
    }
    badge.hidden = currentAccount.ready;
    badge.textContent = "Example details only. No money can be sent using this information.";
    const fields = document.querySelector("#account-fields");
    fields.replaceChildren();
    fieldsFor(currentAccount).forEach(([key, label, example]) => {
      const row = document.createElement("div");
      row.className = "account-field";
      const group = document.createElement("div");
      const term = document.createElement("dt");
      term.textContent = label;
      const value = document.createElement("dd");
      value.textContent = currentAccount.ready ? currentAccount[key] : example;
      group.append(term, value);
      row.append(group);
      if (currentAccount.ready) {
        const copy = document.createElement("button");
        copy.className = "copy-button";
        copy.type = "button";
        copy.textContent = "Copy";
        copy.setAttribute("aria-label", `Copy ${label.toLowerCase()}`);
        const text = currentAccount[key];
        copy.addEventListener("click", () => copyText(text));
        row.append(copy);
      }
      fields.append(row);
    });
    document.querySelector("#download-details").textContent = currentAccount.ready
      ? "Save transfer instructions ↓" : "Save example instructions ↓";
    dialog.showModal();
    document.body.classList.add("modal-open");
  });
});

function closeDialog() { dialog.close(); }
document.querySelector(".dialog-close").addEventListener("click", closeDialog);
document.querySelector(".dialog-done").addEventListener("click", closeDialog);
dialog.addEventListener("click", event => {
  const box = dialog.getBoundingClientRect();
  if (event.target === dialog && (event.clientX < box.left || event.clientX > box.right || event.clientY < box.top || event.clientY > box.bottom)) closeDialog();
});
dialog.addEventListener("close", () => {
  document.body.classList.remove("modal-open");
  opener?.focus();
});

document.querySelector("#download-details").addEventListener("click", () => {
  if (!currentAccount) return;
  const heading = currentAccount.ready ? "BANK TRANSFER INSTRUCTIONS" : "EXAMPLE ONLY — DO NOT SEND MONEY";
  const lines = ["Jesus Oneness Love Mission", heading, "", currentAccount.label, ""];
  fieldsFor(currentAccount).forEach(([key, label, example]) => lines.push(`${label}: ${currentAccount.ready ? currentAccount[key] : example}`));
  lines.push("", "Make any actual transfer through your own bank after checking the recipient.", "Keep your bank receipt. Downloading these instructions does not make a donation.");
  const url = URL.createObjectURL(new Blob([lines.join("\n")], {type:"text/plain;charset=utf-8"}));
  const anchor = document.createElement("a");
  anchor.href = url;
  anchor.download = `jolm-${currentAccount.id}-${currentAccount.ready ? "transfer" : "example"}.txt`;
  document.body.append(anchor);
  anchor.click();
  anchor.remove();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
  toast(currentAccount.ready ? "Transfer instructions saved." : "Example instructions saved.");
});

const events = JSON.parse(document.querySelector("#events-data").textContent);
const filters = document.querySelectorAll("[data-filter]");
const eventCards = document.querySelectorAll(".event-card");
filters.forEach(button => button.addEventListener("click", () => {
  const selected = button.dataset.filter;
  filters.forEach(filter => {
    const active = filter === button;
    filter.classList.toggle("active", active);
    filter.setAttribute("aria-pressed", String(active));
  });
  let count = 0;
  eventCards.forEach(card => {
    card.hidden = selected !== "all" && card.dataset.category !== selected;
    if (!card.hidden) count++;
  });
  document.querySelector("#filter-status").textContent = `${count} ${count === 1 ? "event" : "events"} shown`;
}));

const gallery = document.querySelector("#gallery-dialog");
const galleryImage = document.querySelector("#gallery-image");
const imageBase = new URL(".", galleryImage.src);
let currentEvent;
let photoIndex = 0;
let galleryOpener;
function showPhoto() {
  const photo = currentEvent.photos[photoIndex];
  galleryImage.src = new URL(photo.file, imageBase).href;
  galleryImage.alt = photo.alt;
  document.querySelector("#gallery-caption").textContent = `${photoIndex + 1} / ${currentEvent.photos.length} — ${photo.alt}`;
}
function movePhoto(direction) {
  photoIndex = (photoIndex + direction + currentEvent.photos.length) % currentEvent.photos.length;
  showPhoto();
}
document.querySelectorAll(".gallery-open").forEach(button => button.addEventListener("click", () => {
  currentEvent = events.find(event => event.id === button.dataset.event);
  if (!currentEvent) return;
  photoIndex = 0;
  galleryOpener = button;
  document.querySelector("#gallery-title").textContent = currentEvent.title;
  showPhoto();
  gallery.showModal();
  document.body.classList.add("modal-open");
}));
document.querySelector("#gallery-prev").addEventListener("click", () => movePhoto(-1));
document.querySelector("#gallery-next").addEventListener("click", () => movePhoto(1));
document.querySelector(".gallery-close").addEventListener("click", () => gallery.close());
gallery.addEventListener("keydown", event => {
  if (event.key === "ArrowRight") {event.preventDefault();movePhoto(1);}
  if (event.key === "ArrowLeft") {event.preventDefault();movePhoto(-1);}
});
gallery.addEventListener("click", event => {
  const box = gallery.getBoundingClientRect();
  if (event.target === gallery && (event.clientX < box.left || event.clientX > box.right || event.clientY < box.top || event.clientY > box.bottom)) gallery.close();
});
gallery.addEventListener("close", () => {
  document.body.classList.remove("modal-open");
  galleryOpener?.focus();
});

// Video facades. The poster is a plain image and a button; the YouTube player is
// only created once a visitor presses play. Nothing is requested from YouTube —
// and no YouTube cookie is set — for the many people who never watch.
document.querySelectorAll(".video-play").forEach(button => {
  button.addEventListener("click", () => {
    const id = button.dataset.video;
    if (!id) return;
    const frame = document.createElement("iframe");
    frame.className = "video-frame";
    frame.src = `https://www.youtube-nocookie.com/embed/${encodeURIComponent(id)}?autoplay=1&rel=0&modestbranding=1`;
    frame.title = button.dataset.title || "Video";
    frame.allow = "accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture";
    frame.allowFullscreen = true;
    button.replaceWith(frame);
  });
});
