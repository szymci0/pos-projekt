Cypress.Commands.add('login', (email="test@test.com", pw="kjnakjnsas") => {
    cy.visit("account/login_management");
    cy.get('input[name="login"]').type(email).should("have.value", email);
    cy.get('input[name="password"]')
      .type(pw)
      .should("have.value", pw)
    cy.get('[data-cy=login-button]').click()
    cy.url().should("not.include", "login");
})