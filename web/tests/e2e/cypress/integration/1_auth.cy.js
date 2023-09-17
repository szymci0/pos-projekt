context("Auth", () => {
    it("Login", () => {
        cy.login();
    });

    it("Logout", () => {
        cy.get('[data-cy="logout"]').click();
        cy.url().should("include", "login");
    });
})