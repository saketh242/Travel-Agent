const form = document.getElementById("plan-form");
const queryInput = document.getElementById("query");
const submitBtn = document.getElementById("submit-btn");
const btnLabel = submitBtn.querySelector(".btn-label");
const spinner = submitBtn.querySelector(".spinner");
const errorEl = document.getElementById("error");
const resultSection = document.getElementById("result");
const planOutput = document.getElementById("plan-output");
const card = document.querySelector(".card");

const apiBase =
  window.location.host.endsWith(":5173") || window.location.protocol === "file:"
    ? "http://127.0.0.1:8000"
    : window.location.origin;
const apiUrl = `${apiBase}/api/plan`;

document.querySelectorAll(".chip").forEach((chip) => {
  chip.addEventListener("click", () => {
    queryInput.value = chip.dataset.example || "";
    queryInput.focus();
  });
});

function setLoading(loading) {
  submitBtn.disabled = loading;
  spinner.hidden = !loading;
  btnLabel.textContent = loading ? "Planning…" : "Generate plan";
}

function showError(message) {
  errorEl.textContent = message;
  errorEl.hidden = !message;
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  showError("");
  resultSection.hidden = true;

  const query = queryInput.value.trim();
  if (!query) {
    showError("Please describe your trip.");
    return;
  }

  setLoading(true);

  try {
    const response = await fetch(apiUrl, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ query }),
    });

    const data = await response.json().catch(() => ({}));

    if (!response.ok) {
      const detail = data.detail;
      const message = Array.isArray(detail)
        ? detail.map((item) => item.msg || item).join(" ")
        : detail;
      throw new Error(message || "Something went wrong. Try again.");
    }

    planOutput.textContent = data.plan || "";
    resultSection.hidden = false;
    card.classList.add("has-result");
    resultSection.scrollIntoView({ behavior: "smooth", block: "nearest" });
  } catch (err) {
    showError(err.message || "Failed to reach the server.");
  } finally {
    if (resultSection.hidden) {
      card.classList.remove("has-result");
    }
    setLoading(false);
  }
});
