const output = document.getElementById("output");
const apiBaseInput = document.getElementById("apiBase");
const healthBtn = document.getElementById("healthBtn");

function setOutput(text) {
  output.textContent = text;
}

healthBtn.addEventListener("click", async () => {
  const baseUrl = apiBaseInput.value.replace(/\/$/, "");
  const url = `${baseUrl}/health`;

  setOutput("Checking API...");

  try {
    const response = await fetch(url, { cache: "no-store" });
    const text = await response.text();

    setOutput(
      `Request: ${url}\n\nStatus: ${response.status}\n\nResponse:\n${text}`
    );
  } catch (error) {
    setOutput(`Error:\n${error.message}`);
  }
});
