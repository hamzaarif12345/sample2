let users = [];

function saveUser() {
    const username = document.getElementById('username').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const userId = document.getElementById('userId').value;

    if (!validateForm(username, email, password)) {
        return;
    }

    const user = {
        id: userId || generateUserId(),
        username,
        email,
        password
    };

    if (userId) {
        // Update existing user
        const index = users.findIndex(u => u.id === userId);
        users[index] = user;
    } else {
        // Create new user
        users.push(user);
    }

    clearForm();
    displayUsers();
}

function deleteuser(userId) {
    users = users.filter(user => user.id !== userId);
    displayUsers();
}

function editUser(userId) {
    const user = users.find(user => user.id === userId);
    if (user) {
        document.getElementById('username').value = user.username;
        document.getElementById('email').value = user.email;
        document.getElementById('password').value = user.password;
        document.getElementById('userId').value = user.id;
    }
}

function validateForm(username, email, password) {
    if (!username || !email || !password) {
        alert('All fields are required!');
        return false;
    }

    if (!isValidEmail(email)) {
        alert('Invalid email address!');
        return false;
    }

    return true;
}

function isValidEmail(email) {
    // Basic email validation
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

function generateUserId() {
    // Simple unique ID generation
    return Math.random().toString(36).substr(2, 9);
}

function clearForm() {
    document.getElementById('username').value = '';
    document.getElementById('email').value = '';
    document.getElementById('password').value = '';
    document.getElementById('userId').value = '';
}

function displayUsers() {
    const userListDiv = document.getElementById('userList');
    userListDiv.innerHTML = '';

    users.forEach(user => {
        const userDiv = document.createElement('div');
        userDiv.className = 'user';

        const userInfo = `
            <p><strong>Username:</strong> ${user.username}</p>
            <p><strong>Email:</strong> ${user.email}</p>
            <button onclick="editUser('${user.id}')">Edit</button>
            <button onclick="deleteuser('${user.id}')">Delete</button>
        `;

        userDiv.innerHTML = userInfo;
        userListDiv.appendChild(userDiv);
    });
}

// Initial display
displayUsers();
