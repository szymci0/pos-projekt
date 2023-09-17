describe("Auth", () => {
    it("Login - Logout", () => {
        cy.login();
        cy.get('[data-cy="logout"]').click();
        cy.url().should("include", "login");
    });
})