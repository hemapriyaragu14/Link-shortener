document.getElementById('shorten-form').addEventListener('submit', function (e) {
    e.preventDefault();
    const longURL = e.target.elements.long_url.value;
    fetch('/shorten', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ long_url: longURL }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('shortened-url').innerHTML = `Shortened URL: <a href="${data.short_url}">${data.short_url}</a>`;
    });
});
