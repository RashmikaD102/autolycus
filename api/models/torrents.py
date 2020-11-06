from shared.factories import db

class Torrent(db.Model):
    __tablename__ = 'torrents'
    id = db.Column(db.Integer, primary_key=True)

    # Torrent related information
    name = db.Column(db.String)
    added_time = db.Column(db.Integer) # epoch time
    download_path = db.Column(db.String)
    magnet = db.Column(db.String)
    Hash = db.Column(db.String)

    # File size related information
    total_bytes = db.Column(db.Integer) #Bytes
    downloaded_bytes = db.Column(db.Integer) #Bytes

    # connection related information
    num_connections = db.Column(db.Integer)
    num_peers = db.Column(db.Integer)
    num_seeds = db.Column(db.Integer)
    num_trackers = db.Column(db.Integer)

    # speed realted information
    upload_speed = db.Column(db.Integer) #Bytes/s
    download_speed = db.Column(db.Integer) #Bytes/s

    # Progress related information
    queue_position = db.Column(db.Integer)
    progress = db.Column(db.Integer)
    is_paused = db.Column(db.Boolean)
    is_finished = db.Column(db.Boolean)

    @classmethod
    def find_by_hash(self, Hash):
        return self.query.filter_by(Hash=Hash).first()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def update_to_db(self, fields, synchronize_session = False):
        db.session.query(Torrent).filter(Torrent.Hash == self.Hash).update(
            fields, synchronize_session=synchronize_session)
        db.session.commit()

    @property
    def JSON(self):
        return {
        "added_time": self.added_time,
        "download_path": self.download_path,
        "download_speed": self.download_speed,
        "downloaded_bytes": self.downloaded_bytes,
        "hash": self.Hash,
        "magnet": self.magnet,
        "is_finished": self.is_finished,
        "is_paused": self.is_paused,
        "name": self.name,
        "num_connections": self.num_connections,
        "num_peers": self.num_peers,
        "num_seeds": self.num_seeds,
        "num_trackers": self.num_trackers,
        "progress": self.progress,
        "queue_position": self.queue_position,
        "total_bytes": self.total_bytes,
        "upload_speed": self.upload_speed
        }
        
    def __repr__(self):
       return str(self.json)