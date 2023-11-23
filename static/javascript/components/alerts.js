/* Sourced alert HTML from
https://getbootstrap.com/docs/5.2/components/alerts/
 */

function SuccessAlert(message) {
  return (
      <div className="alert alert-success" role="alert">
          {message}
      </div>
  )
}

function WarningAlert(message) {
  return (
      <div className="alert alert-warning" role="alert">
          {message}
      </div>
  )
}

function ErrorAlert(message) {
  return (
      <div className="alert alert-danger" role="alert">
          {message}
      </div>
  )
}