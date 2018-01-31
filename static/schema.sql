DROP TABLE IF EXISTS event;
CREATE TABLE event
(
  id              VARCHAR(12) PRIMARY KEY, /* random */
  title           TEXT NOT NULL,
  organization    TEXT NOT NULL,
  start_date      DATE NOT NULL,
  start_time      TIME NOT NULL,
  end_date        DATE NOT NULL,
  end_time        TIME NOT NULL,
  cost            INTEGER DEFAULT 0,
  contact_name    TEXT NOT NULL,
  contact_email   TEXT NOT NULL,
  contact_phone   TEXT NOT NULL,
  url             TEXT DEFAULT NULL,
  has_photo       INTEGER DEFAULT 0,
  password        TEXT NOT NULL,
  created_at      DATETIME DEFAULT CURRENT_TIMESTAMP
);


DROP TABLE IF EXISTS category;
CREATE TABLE category
(
  id              VARCHAR(12) PRIMARY KEY, /* random */
  title           TEXT NOT NULL,
  created_at      DATETIME DEFAULT CURRENT_TIMESTAMP
);


DROP TABLE IF EXISTS event_category;
CREATE TABLE event_category
(
  event_id       INTEGER REFERENCES event (id),
  category_id    INTEGER REFERENCES category (id),
  created_at     DATETIME DEFAULT CURRENT_TIMESTAMP
);
