let data = fs.readFileSync('media.json');
function searchengine() {
    var search_prompt = document.getElementById("searchbar").value;
    media_id = data[search_prompt][1];
    document.getElementById("titlea").style.display = "none";
    document.getElementById("titleam").style.display = "none";
    document.getElementById("titlem").style.display = "none";
    document.getElementById("titletvs").style.display = "none";
    document.getElementById("dummya").style.display = "none";
    document.getElementById("dummyam").style.display = "none";
    document.getElementById("dummym").style.display = "none";
    document.getElementById("dummytvs").style.display = "none";
    document.getElementById(media_id).style.display = "block";
}