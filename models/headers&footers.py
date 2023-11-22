class FooterModel:

    @staticmethod
    def basic_footer() -> str:
        return f"""
        <div class="fixed-bottom bg-primary" style="--bs-bg-opacity: .175;">

            <div class="container text-center">
              <div class="row align-items-center">
                <div class="col justify-items-start">
                  <a class="footer-logo" href="#">
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
                          <a class="contacts-links" href="#">
                              example@example.co.uk
                          </a>
                      </li>
                      <li class="contacts-text">
                          Phone:
                          <a class="contacts-links" href="#">
                              0777777777
                          </a>
                      </li>
                      <li class="contacts-text">
                          Address:
                          <a class="contacts-links" href="#">
                              Example Address
                          </a>
                      </li>
                    </ul>
                </div>
              </div>
            </div>

        </div>"""

class HeaderModel:

    @staticmethod
    def basic_header() -> str:
        return f"""
        <nav class="navbar bg-primary" style="--bs-bg-opacity: .175;">

                <ul class="nav justify-content-start">
                    <a class="header-logo" href="#">
                        <img class="logo" src="../static/images/logo-temp.png"  alt="" width="45" height="45">
                    </a>
                </ul>

                <ul class="nav justify-content-end">
                    <button class="options-btn bg-primary" style="--bs-bg-opacity: .0;" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasRight" aria-controls="offcanvasRight">
                        <img class="options-btn-image" src="../static/images/burger.png" alt="" width="32" height="32">
                    </button>
                </ul>

                    <div class="offcanvas offcanvas-end bg-secondary" tabindex="-1" id="offcanvasRight" aria-labelledby="offcanvasRightLabel">
                      <div class="offcanvas-header">
                        <h5 class="offcanvas-title" id="offcanvasRightLabel">Menu</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
                      </div>

                      <div class="offcanvas-body">
                        <ul class="options-list">
                            <li>
                                <a class="menu-links" href="#">
                                    Log In
                                </a>
                            </li>
                            <li>
                                <a class="menu-links" href="#">
                                    Sign Up
                                </a>
                            </li>
                        </ul>
                      </div>
                    </div>
        </nav>"""

    @staticmethod
    def logged_header() -> str:
        return f"""
        <nav class="navbar bg-primary" style="--bs-bg-opacity: .175;">

            <ul class="nav justify-content-start">
                <a class="header-logo" href="#">
                    <img class="logo" src="../static/images/logo-temp.png"  alt="" width="45" height="45">
                </a>
            </ul>

            <ul class="nav justify-content-end">
                <button class="options-btn bg-primary" style="--bs-bg-opacity: .0;" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasRight" aria-controls="offcanvasRight">
                    <img class="options-btn-image" src="../static/images/blank-pfp.png" alt="" width="32" height="32">
                </button>
            </ul>

                <div class="offcanvas offcanvas-end bg-secondary" tabindex="-1" id="offcanvasRight" aria-labelledby="offcanvasRightLabel">
                  <div class="offcanvas-header">
                    <h5 class="offcanvas-title" id="offcanvasRightLabel">Menu</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
                  </div>

                  <div class="offcanvas-body">
                    <ul class="options-list">
                        <li>
                            <a class="menu-links" href="#">
                                Account
                            </a>
                        </li>
                        <li>
                            <a class="menu-links" href="#">
                                Settings
                            </a>
                        </li>
                        <li>
                            <a class="menu-links" href="#">
                                Log Out
                            </a>
                        </li>
                    </ul>
                  </div>
                </div>
        </nav>"""