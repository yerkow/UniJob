document.getElementById('tab-user').onclick = function(){
    this.classList.add('active')
    document.getElementById('tab-org').classList.remove('active');
}

document.getElementById('tab-org').onclick = function(){
    this.classList.add('active')
    document.getElementById('tab-user').classList.remove('active');
}

// Переключение между входом и регистрацией с анимацией
document.getElementById('show-register').onclick = function() {
    document.getElementById('login-form').classList.add('hidden');
    document.getElementById('register-form').classList.remove('hidden');
};
document.getElementById('show-login').onclick = function() {
    document.getElementById('register-form').classList.add('hidden');
    document.getElementById('login-form').classList.remove('hidden');
};

document.getElementById('github-login').onclick = function() {
    window.location.href = '/auth/github/login?type=' + 
        (document.getElementById('tab-org').classList.contains('active') ? 'org' : 'user');
};

document.getElementById('github-register').onclick = function() {
    window.location.href = '/auth/github/login?type=' + 
        (document.getElementById('tab-org').classList.contains('active') ? 'org' : 'user');
};