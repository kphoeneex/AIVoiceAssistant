let mediaRecorder;
let chunks = [];
let stream;


function startApp() {
      const intro = document.getElementById("intro");
      intro.classList.add("fade-out");
    }

async function startMic() {
  const status = document.getElementById("status");

  try {
    stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    mediaRecorder = new MediaRecorder(stream);
    chunks = [];

    mediaRecorder.ondataavailable = e => chunks.push(e.data);
    mediaRecorder.onstop = sendRecording;

    mediaRecorder.start();
    status.textContent = "🎙️ Recording... Hold the mic button";
  } catch (err) {
    console.error(err);
    status.textContent = "Microphone access denied or error.";
  }
}

function stopMic() {
  if (mediaRecorder && mediaRecorder.state === "recording") {
    mediaRecorder.stop();
    stream.getTracks().forEach(track => track.stop());
    document.getElementById("status").textContent = "🛑 Stopped. Processing...";
  }
}

function sendRecording() {
  const blob = new Blob(chunks, { type: 'audio/webm' });
  const formData = new FormData();
  formData.append("audio", blob, "recording.webm");

  fetch("http://127.0.0.1:5000/process", {
    method: "POST",
    body: formData
  })
  .then(res => res.json())
  .then(data => {
    document.getElementById("status").textContent = `🧠 ${data.reply_text}`;

    const audio = new Audio("http://127.0.0.1:5000" + data.reply_audio_url);
    audio.play();
  })
  .catch(() => {
    document.getElementById("status").textContent = "❌ Error sending audio.";
  });
}

