describe("Users", () => {
    before(() => {
        cy.login()
        cy.saveLocalStorage();
    });

    beforeEach(() => {
        cy.restoreLocalStorage();
    });

    it("Users table", () => {
        cy.get('[data-cy="UsersNav"]')
            .should("be.visible")
            .click()
        
        cy.wait(2000);

        cy.get('input[placeholder="Search query"]')
            .type("test@test.com{enter}")
        
        cy.get('.VuePagination__count')
            .should("contain.text", "One record")
    })
})