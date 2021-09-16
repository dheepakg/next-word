# next-word

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![Build Status](https://app.travis-ci.com/dheepakg/next-word.svg?branch=main)](https://app.travis-ci.com/dheepakg/next-word)

[![codecov](https://codecov.io/gh/dheepakg/next-word/branch/main/graph/badge.svg?token=8GNZB1J8L4)](https://codecov.io/gh/dheepakg/next-word)

Suggests next word based on your typing history.

The project is to clone the auto-suggest functionality provided by popular keyboards for handheld devices - phone/tablets.

### How does it work?

1. We provide a paragraph.

2. System will assign weightage to words based on the order.
   Example,

   > sample text = "My name is John. My hobby is running. My hobby is what I like to do daily."

| Word | followed by - 1 | followed by - 2 | followed by - 3 |
| ---- | --------------- | --------------- | --------------- |
| My   | hobby           | name            | -               |

Here, after typing `My`, system will suggest `hobby`(1<sup>st</sup> choice) and `name` (2<sup>nd</sup> choice).
