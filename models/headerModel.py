class HeaderModel:

    @staticmethod
    def renderHeader(session) -> str:
        if "UserID" in session:
            return HeaderModel.loggedInHeader()
        else:
            return HeaderModel.standardHeader()

    @staticmethod
    def standardHeader() -> str:
        return f"""
        <nav class="navbar bg-primary" style="--bs-bg-opacity: .175;">

                <ul class="nav justify-content-start">
                    <a class="header-logo" href="/home">
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
                                <a class="menu-links" href="/login">
                                    Log In
                                </a>
                            </li>
                            <li>
                                <a class="menu-links" href="/register">
                                    Sign Up
                                </a>
                            </li>
                        </ul>
                      </div>
                    </div>
        </nav>"""

    @staticmethod
    def loggedInHeader() -> str:
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
                            <a class="menu-links" href="/account">
                                Account
                            </a>
                        </li>
                        <li>
                            <a class="menu-links" href="/settings">
                                Settings
                            </a>
                        </li>
                        <li>
                            <a class="menu-links" href="/logout">
                                Log Out
                            </a>
                        </li>
                    </ul>
                  </div>
                </div>
        </nav>"""