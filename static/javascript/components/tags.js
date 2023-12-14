class Tags {
    // Function that renders a tag pill with a name and colour
    static render(name, colour) {
        return `
        <span class="badge rounded-pill" style="background-color: ${colour};">${name}</span>
        `;
    }
}