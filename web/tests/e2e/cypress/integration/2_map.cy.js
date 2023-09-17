context("Map", () => {
    before(() => {
        cy.login();
        cy.saveLocalStorage();
    });

    it("Search county", () => {
        cy.get('[data-cy="county-search"]')
            .should("be.visible")
            .type("Gniew")
        
        cy.get('[data-cy="search-button"]')
            .should("be.visible")
            .click()
        
        cy.wait(1000)
        
        cy.get('[id="2214023"]')
            .should("have.css", "fill", "rgb(255, 0, 0)")
            
    })
})