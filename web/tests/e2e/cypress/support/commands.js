let LOCAL_STORAGE_MEMORY = {};

Cypress.Commands.add("saveLocalStorage", () => {
    Object.keys(localStorage).forEach((key) => {
      LOCAL_STORAGE_MEMORY[key] = localStorage[key];
    });
});

Cypress.Commands.add("restoreLocalStorage", () => {
    Object.keys(LOCAL_STORAGE_MEMORY).forEach((key) => {
      localStorage.setItem(key, LOCAL_STORAGE_MEMORY[key]);
    });
});

Cypress.Commands.add("clearSavedLocalStorage", () => {
    LOCAL_STORAGE_MEMORY = {}
    localStorage.clear()
});

Cypress.Commands.add('login', (email="test@test.com", pw="kjnakjnsas") => {
    cy.visit("account/login_management");
    cy.get('input[type="email"]').type(email).should("have.value", email);
    cy.get('input[type="password"]')
      .type(pw)
      .should("have.value", pw)
    cy.get('[data-cy=login-button]').click()
    cy.url().should("not.include", "login");
})