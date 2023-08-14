// your_script.js

const form = document.getElementById('question-form');
const questionInput = document.getElementById('question-input');
const answerContainer = document.getElementById('answer-container');

form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const question = questionInput.value;

    // 使用OpenAI API发送问题并获取回答
    const apiKey = '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';
    const response = await fetch('https://api.openai.com/v1/engines/davinci-codex/completions', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${apiKey}`, // 使用 "Bearer" 授权
    },
    body: JSON.stringify({
        prompt: question,
        max_tokens: 50,
    }),
});

    const data = await response.json();
    const answer = data.choices[0].text;

    // 将回答显示在网页上
    answerContainer.innerHTML = `<p><strong>回答：</strong>${answer}</p>`;
});
