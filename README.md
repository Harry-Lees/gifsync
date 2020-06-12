[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Septem151/gifsync">
    <img src="gifsync/static/images/logo.png" alt="GifSync Logo" width="256" height="256">
  </a>

  <h3 align="center"><a href="https://gifsync.herokuapp.com">GifSync</a></h3>

  <p align="center">
    Synchronize the speed of Gifs to music on Spotify in real time
    <br />
    <br />
    <br />
    <a href="https://github.com/Septem151/gifsync/issues">Report Bug</a>
    ·
    <a href="https://github.com/Septem151/gifsync/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
  * [Making Changes](#making-changes)
* [License](#license)
* [Contact](#contact)



<!-- ABOUT THE PROJECT -->
## About The Project
<!-- EXCLUDE PROJECT SCREENSHOT
[![GifSync Screen Shot][project-screenshot]](https://example.com)
-->
GifSync started out as a simple question: "How do I get [Hat Kid][hatintime-url] to dance to my music while I stream?" The answer to this question quickly turned into a long and convoluted dive into APIs, gif frame-times, and web servers.

However, through the power of **THE INTERNET!!** (and a ton of duck-duck-go'ing) I was able to pull it off with as best of accuracy as I could. Best of all, it works with any gif! I wanted to share this with others so that no matter what your experience level is in programming, you too can experience gifs that dance to your music in real time.


### Built With

* [Python][python-url]
* [Flask][flask-url]
* [Bootstrap][bootstrap-url]
* [Heroku][heroku-url]

<!-- USAGE EXAMPLES -->
## Usage
GifSync is hosted on [Heroku][heroku-url]. The link for GifSync is https://gifsync.herokuapp.com


<!-- ROADMAP -->
## Roadmap
| Release Version | Release Date | Status |
| :-------------: | :----------: | :-------: |
| HTML Skeleton | TBD | IN PROGRESS |
| Event Handling | TBD | |
| Database Integration | TBD | |
| Alpha Release | TBD | |
| Beta Release | TBD | |
| Full Release | TBD | |

See the [open issues][issues-url] for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions make the world go round, and I am by no means perfect. In fact, a lot of the tools used for this project are new to me. Any contributions you make are **greatly appreciated**, whether it's help with coding, security, bug fixes, or user feedback.

### Prerequisites

If you plan on testing any functionality involving the Spotify API, you need to have a [registered App with Spotify][spotifydev-url] in order to get a Client ID and Client Secret.

* Python 3 and Pip
    ```sh
    sudo apt update && sudo apt upgrade
    sudo apt install python3 python3-pip
    python3 -m pip install --upgrade pip
    ```

### Installation
 
1. Fork the Repository on GitHub
    * It is recommended that you fork the repository so you can push changes and submit pull requests.

2. Clone the forked Repository locally
    ```sh
    git clone https://github.com/YOUR-USERNAME/gifsync.git
    cd gifsync
    ```

2. (Optional) Create a Python virtual environment
    ```sh
    sudo apt update
    sudo apt install python3-venv
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install required modules
    ```sh
    python3 -m pip install -r requirements.txt
    ```

4. Run the server
    ```sh
    python3 -m run
    ```

### Making Changes
1. Create your Feature Branch (`git checkout -b feature/SomeFeature`)
2. Make some changes and stage them (`git add .`)
3. Commit your Changes (`git commit -m 'Add some Feature'`)
    - If you make multiple commits, please [squash them][squash-url] into a single commit before Pushing or opening a Pull request
4. Push to the Branch (`git push origin feature/SomeFeature`)
5. Open a Pull Request on GitHub



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Carson Mullins ([Septem 151][keybase-url]) - [septem151@protonmail.com][email-mailto]

Project Link: https://github.com/Septem151/gifsync


<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [Gears for Breakfast][gfb-url]
  * For making an amazing game, whose protagonist is in the GifSync logo


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Septem151/gifsync.svg?style=flat-square
[contributors-url]: https://github.com/Septem151/gifsync/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Septem151/gifsync.svg?style=flat-square
[forks-url]: https://github.com/Septem151/gifsync/network/members
[stars-shield]: https://img.shields.io/github/stars/Septem151/gifsync.svg?style=flat-square
[stars-url]: https://github.com/Septem151/gifsync/stargazers
[issues-shield]: https://img.shields.io/github/issues/Septem151/gifsync.svg?style=flat-square
[issues-url]: https://github.com/Septem151/gifsync/issues
[license-shield]: https://img.shields.io/github/license/Septem151/gifsync.svg?style=flat-square
[license-url]: https://github.com/Septem151/gifsync/blob/master/LICENSE.txt
[project-screenshot]: gifsync/static/images/screenshot.png
[hatintime-url]: https://gearsforbreakfast.com/games/a-hat-in-time/
[gfb-url]: https://gearsforbreakfast.com
[python-url]: https://www.python.org/
[flask-url]: https://pypi.org/project/Flask/
[heroku-url]: https://heroku.com
[bootstrap-url]: https://getbootstrap.com
[squash-url]: https://stackoverflow.com/questions/5189560/squash-my-last-x-commits-together-using-git
[keybase-url]: https://keybase.io/septem151
[email-mailto]: mailto:septem151@protonmail.com
[spotifydev-url]: https://developer.spotify.com/dashboard/login