<a name="readme-top"></a>

[![LinkedIn][linkedin-shield]][linkedin-url]
</br>
A log ingestor system that can efficiently handle vast volumes of log data, and offer a simple interface for querying this data using full-text search or specific field filters.
<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

* Used Docker to ensure Consistency and Scalability
* Used postgresql with Indexing to increase search efficiency


### Built With

* [![Laravel][Laravel.com]][Laravel-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]
* [![Docker][Docker.com]][docker-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Using docker i have made it very easy to run and use the project. 

### Prerequisites

* Docker

  1. Install docker from  [https://www.docker.com/](https://www.docker.com/)
 

### Installation


1. Clone the repo
   ```sh
   git clone https://github.com/dyte-submissions/november-2023-hiring-ain-py.git
   ```
2. Build the Docker Container
   ```sh
   docker-compose build
   ```
3. Run Docker container in background
   ```sh
   docker-compose up -d
   ```
3. Run the following commands to apply migrations to create the necessary tables in PostgreSQL database:
   ```sh
   docker-compose exec web flask db upgrade
   ```
4. Server will be live at 
   ```sh
   http://localhost:3000/
   ```

5. To STOP SERVER RUN 
   ```sh
   docker-compose down
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

#### View all logs
```http
  GET /
```
#### Search logs
```http
  GET /search
```

#### Add log

```http
  POST /add_log
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `log_data` | `string` | **Required**: Json data of log |

ex:
```sh
log_data = {
    "level": "WRYE",
"message": "X6L6V8J",
"resourceId": "server-T6L", 
"timestamp": "2022-03-10T23:02:36Z",
"traceId": "abc-AWG-123",
"spanId": "span-WRYE",
"commit": "5e5342f",
"metadata": {"parentResourceId": "server-X8"}}
```

#### Add log through script (check this file)

```sh
   app/test/populate.py
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Features implemented

- [x] Offer a user interface (Web UI or CLI) for full-text search across logs.
- [x] Include filters based on: level,message,resourceId,timestamp,traceId,spanId,commit
- [x] Implement search within specific date ranges.(BONUS)
- [x] Allow combining multiple filters.(BONUS)
- [x] Provide real-time log ingestion and searching capabilities.(BONUS)
- [x] Provide real-time log ingestion and searching(BONUS) 


<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/noor-e-ain/
[product-screenshot]: images/pic1.png

[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Flask-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://flask.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[Docker.com]: https://img.shields.io/badge/docker-0769AD?style=for-the-badge&logo=docker&logoColor=white
[Docker-url]: https://docker.com

