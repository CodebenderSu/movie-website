import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <title>Juicy Apples</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.1/js/bootstrap.min.js"></script>
    <!-- CSS Classes -->
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
            background-image: url("https://entp-tender-production.s3.amazonaws.com/assets/a67cf7e57cc2088e60606615ffcc003f1f886341/RedCurtains.jpg?AWSAccessKeyId=AKIAISVUXXOK32ATONEQ&Expires=1820818831&Signature=QE6bg73NoVpMmRlaq675Epz7%2BuU%3D");
            background-repeat: no-repeat;
            background-position: center;
            background-color: #000;
            background-size: cover;
            background-attachment: fixed;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 100%;
            max-width: 640px;
            height: auto;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 40px;
            padding-top: 40px;
            color: #ffe;
        }
        .movie-poster {
            position: relative;
            width: 220px;
            height: 342px;
            margin: auto;
        }
        .movie-poster img {
            width: 220px;
            height: 342px;
            transition: all 0.2s linear;
            -moz-transition: all 0.2s linear;
            -webkit-transition: all 0.2s linear;
            -ms-transition: all 0.2s linear;
            -o-transition: all 0.2s linear;
        }
        .movie-poster:hover img {
            transform:scale(1.085);
            -moz-transform:scale(1.085);
            -webkit-transform:scale(1.085);
            -ms-transform:scale(1.085);
            -o-transform:scale(1.085);
        }
        .movie-poster:hover .movie-info {
            visibility: visible;
            transform:scale(1.085);
            -moz-transform:scale(1.085);
            -webkit-transform:scale(1.085);
            -ms-transform:scale(1.085);
            -o-transform:scale(1.085);
            cursor: pointer;
        }
        .movie-info {
            transition: all 0.2s ease-in;
            -moz-transition: all 0.2s ease-in;
            -webkit-transition: all 0.2s ease-in;
            -ms-transition: all 0.2s ease-in;
            -o-transition: all 0.2s ease-in;
            visibility: hidden;
            position: absolute;
            top: 0;
            right: 0;
            bottom: 0;
            left: 0;
            background: rgba(0, 0, 0, 0.5);
        }
        .movie-info p {
            color: #d1d1d1;
            font-size: 14px;
        }
        table {
            height: 342px;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
    </style>
    <script type="text/javascript">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''

# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24" alt="Close"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Juicy Apples and Movie Trailers</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {movie_tiles}
    </div>
  </body>
</html>
'''

# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <div class="movie-poster">
        <img src="{poster_image_url}" alt="movie poster image">
        <!-- This is used to overlay the content over the poster images on hover -->
        <div class="movie-info">
            <table>
                <tr>
                    <td class="text-center align-middle">
                        <p style="font-size:18px;color:#fff;">{storyline}</p>
                        <p><b>Rating: {rating}</b></p>
                        <p><b>Length: {length}</b></p>
                    </td>
                </tr>
            </table>
        </div>
    </div>
    <h2>{movie_title}</h2>
</div>
'''

def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title = movie.title,
            poster_image_url = movie.poster_image_url,
            trailer_youtube_id = trailer_youtube_id,
            storyline = movie.storyline,
            rating = movie.rating,
            length = movie.length
        )
    return content

def open_movies_page(movies):
  # Create or overwrite the output file
  output_file = open('fresh_tomatoes.html', 'w')

  # Replace the placeholder for the movie tiles with the actual dynamically generated content
  rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies))

  # Output the file
  output_file.write(main_page_head + rendered_content)
  output_file.close()

  # open the output file in the browser
  url = os.path.abspath(output_file.name)
  webbrowser.open('file://' + url, new=2) # open in a new tab, if possible
