class Buttons {
    static getPastelButton(text, destination, size = 'md') {
        return `<button class="btn btn-pastel btn-${size}" onclick="${destination}">${text}</button>`;
    }

    /* Used Bootstrap documentation for loading button
    Source: https://getbootstrap.com/docs/5.2/components/spinners/ */
    static getPastelButtonLoading(text, size = 'md') {
        return `<button class="btn btn-pastel btn-${size}" type="button" disabled>
                    <span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
                    ${text}
                </button>`;
    }
}