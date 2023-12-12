class FooterModel:

    @staticmethod
    def standardFooter() -> str:
        return f"""
        <div class="bg-primary footer" style="--bs-bg-opacity: .175;">

            <div class="container text-center">
              <div class="row align-items-center">
                <div class="col justify-items-start">
                  <a class="footer-logo" href="/home">
                      <img class="logo" src="../static/images/logo-temp.png"  alt="" width="45" height="45">
                  </a>
                </div>
                <div class="col">
                    <p class="copyright-text"> © 2023 Wavelength. All rights reserved. </p>
                </div>
                <div class="col">
                    <h5 class="title-contacts-text">Contact Us:</h5>
                  <ul class="contacts-list">
                      <li class="contacts-text">
                          Email:
                          <a class="contacts-links" href="example@example.co.uk">
                              example@example.co.uk
                          </a>
                      </li>
                      <li class="contacts-text">
                          Phone:
                          <a class="contacts-links" href="0777777777">
                              0777777777
                          </a>
                      </li>
                      <li class="contacts-text">
                          Address:
                          <a class="contacts-links" href="Example Address">
                              Example Address
                          </a>
                      </li>
                    </ul>
                </div>
              </div>
            </div>

        </div>"""