describe("Map", () => {
    before(() => {
        cy.login();
        cy.saveLocalStorage();
    });

    beforeEach(() => {
        cy.restoreLocalStorage();
    });

    it("County map", () => {
        cy.get('[data-cy="county-search"]')
            .should("be.visible")
            .type("Gniew")
        
        cy.get('[data-cy="search-button"]')
            .should("be.visible")
            .click()
        
        cy.wait(1000)
        
        cy.get('[id="2214023"]')
            .should("have.css", "fill", "rgb(255, 0, 0)")    
        
        cy.get('[id="1465011"]')
            .should("be.visible")
            .click()
        
        cy.get('[data-cy="modal"]')
            .should("be.visible")
        
        cy.get('[data-cy="selected-county"]')
            .should("contain.text", "Warszawa")
        
        cy.get('[data-cy="add-user-input"]')
            .type("test@test.com")
            .should("have.value", "test@test.com")
        
        cy.get('[data-cy="add-user"]')
            .should("be.visible")
            .click()
        
        cy.get('[data-cy="modal"]')
            .should("not.be.visible")

    });
})