// Basic example script to demonstrate dynamic behavior
document.addEventListener('DOMContentLoaded', function() {
    console.log('Blog page loaded');
    
    document.querySelectorAll('.utc-time').forEach(function(element) {
        var utcTime = element.getAttribute('data-utc');
        var localTime = moment.utc(utcTime).local().format('YYYY-MM-DD HH:mm:ss');
        element.textContent = localTime;
    });
});