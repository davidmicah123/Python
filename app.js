async function getData(url) {
    try {
        const res = await fetch(url);
        const data = await res.json();
        console.log(data);
    } catch (err) {
        console.error("Error:", err);
    }
}
class User {
    constructor(name, email) {
        this.name = name;
        this.email = email;
    }
    login() {
        console.log(`${this.name} logged in`);
    }
}
class User {
    constructor(name, email) {
        this.name = name;
        this.email = email;
    }
    login() {
        console.log(`${this.name} logged in`);
    }
}
