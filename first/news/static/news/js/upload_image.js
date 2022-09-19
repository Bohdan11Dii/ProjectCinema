function showPreviewLogo() {
    logo_preview.src=URL.createObjectURL(event.target.files[0]);
}

$('#delete-logo').click(function () {
    $('#id_logo').val("");
    $('#logo_preview').attr("src", "/static/cinema/dist/img/preview_upload.png")
})

function showPreviewBanner() {
    banner_preview.src=URL.createObjectURL(event.target.files[0]);
}

$('#delete-banner').click(function () {
    $('#id_banner').val("");
    $('#banner_preview').attr("src", "/static/cinema/dist/img/preview_upload.png")
})

function showPreviewPoster() {
    poster_preview.src=URL.createObjectURL(event.target.files[0]);
}

$('#delete-poster').click(function () {
    $('#id_poster').val("");
    $('#poster_preview').attr("src", "/static/cinema/dist/img/preview_upload.png")
})