let websites = [];

function addSite() {

    let title = document.getElementById("title").value;
    let link = document.getElementById("link").value;
    let desc = document.getElementById("desc").value;

    websites.push({title, link, desc});

    alert("Website Added!");
}

function search() {

    let query = document.getElementById("searchBox").value.toLowerCase();

    let results = document.getElementById("results");

    results.innerHTML = "";

    websites.forEach(site => {

        if(site.title.toLowerCase().includes(query) ||
           site.desc.toLowerCase().includes(query)) {

            results.innerHTML += `
                <div class="card">
                    <a href="${site.link}" target="_blank">${site.title}</a>
                    <p>${site.desc}</p>
                </div>
            `;
        }
    });
}
