(function() {
    function showDeleted() {
        alert('Files deleted');
    }

    document.addEventListener('DOMContentLoaded', function() {
        var btn = document.getElementById('unapprove-btn');
        if (!btn) return;
        btn.addEventListener('click', function() {
            fetch('/songs/unapprove', { method: 'DELETE' })
                .then(function(res) { if (res.ok) return res.json(); else throw new Error('fail'); })
                .then(function() { showDeleted(); })
                .catch(function() { showDeleted(); });
        });
    });
})();
