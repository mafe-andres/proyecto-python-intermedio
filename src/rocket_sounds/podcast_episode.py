class PodcastEpisode:
    def __init__(self, title, host, podcast, release_date, duration, episode_number, description, guests):
        self.title = title
        self.host = host
        self.podcast = podcast
        self.release_date = release_date
        self.duration = duration
        self.episode_number = episode_number
        self.description = description
        self.guests = guests

    def __str__(self):
        return f"'{self.title}' hosted by {self.host}, Episode {self.episode_number} ({self.release_date})"

    def get_episode_info(self):
        return {
            "Title": self.title,
            "Host": self.host,
            "Podcast": self.podcast,
            "Release Date": self.release_date,
            "Duration": self.duration,
            "Episode Number": self.episode_number,
            "Description": self.description,
            "Guests": self.guests,
        }