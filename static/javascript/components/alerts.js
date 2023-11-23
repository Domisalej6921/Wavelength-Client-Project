/* Sourced alert HTML from
https://getbootstrap.com/docs/5.2/components/alerts/
 */

class Alerts {
    static successAlert(message, subject = "Success!") {
        return `<div class="alert alert-success alert-dismissible fade show" role="alert">
                    <strong>${subject}</strong> ${message}
                    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                </div>`
    }

    static warningAlert(message, subject = "Warning!") {
        return `<div class="alert alert-warning alert-dismissible fade show" role="alert">
                    <strong>${subject}</strong> ${message}
                    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                </div>`
    }

    static errorAlert(message, subject = "Error!") {
        return `<div class="alert alert-danger alert-dismissible fade show" role="alert">
                    <strong>${subject}</strong> ${message}
                    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                </div>`
    }
}