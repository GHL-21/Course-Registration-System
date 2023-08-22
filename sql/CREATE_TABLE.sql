CREATE TABLE `user` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `name` TEXT NOT NULL,
  `email` TEXT NOT NULL,
  `password` TEXT NOT NULL,
  `type` TEXT NOT NULL CHECK(`type` IN ('STUDENT', 'TEACHER', 'ADMIN'))
);

CREATE TABLE `course` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `name` TEXT NOT NULL,
  `credits` INTEGER NOT NULL,
  `term` TEXT NOT NULL,
  `tutor` INTEGER,
  FOREIGN KEY (`tutor`) REFERENCES `user`(`id`)
);

CREATE TABLE `enrolment` (
  `user_id` INTEGER NOT NULL,
  `course_id` INTEGER NOT NULL,
  `enrolled_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (`user_id`) REFERENCES `user`(`id`),
  FOREIGN KEY (`course_id`) REFERENCES `course`(`course_id`)
);
