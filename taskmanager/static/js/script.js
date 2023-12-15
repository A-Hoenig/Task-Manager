document.addEventListener('DOMContentLoaded', function() {
    //sidenav bar initialization
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);

    // datepicker initialization
    let datepicker = document.querySelectorAll('.datepicker');
    M.Datepicker.init(datepicker, {
        format: "dd mmm, yyyy",
        i18n: {done: "Select"}
    });

    // dropdown initialization
    let selects = document.querySelectorAll('select');
    M.FormSelect.init(selects);
  });