The purpose of this project is to develop a means to capture and track the evolution of your creative endeavors. I want to support creatives but giving them the tools to capture all those ideas lost to the long pause between the shower and computer.

## Functionalities

1. Media Capture
    - Users can upload files to the site
    - They will have to enter metadata and classify the file

2. Media Enrichment
    - Users can enter notes to be linked with a file
    - Users can tag files with feelings/vibes

3. Lineage Exploration (not core)
    - Users can explore the graph of their created files
    - User -> file/idea -> revision 1 of idea -> ... -> revision n of idea
    - lastest revision inherits/sets vibes of branch, original attributes are saved
4. Graph queries (non core)
    - Users can ask to be served an unfinished idea or manually filter by attributes

5. Idea generation
    - Users can ask to have an idea generated to some extent, via some LLM type service


## Schema

- User: Account ID, Pass
- Idea: hasUser, Lyric, Music, Note: string, Rev Number: int
    - Lyric: Doc, string
        - Doc: .doc, .text
    - Music: MIDI, Score, MP3/M4A
        - MIDI: .MID
        - Score: ???

    ### Example Schema: *One User, Two Ideas*
    ```json
    {
        "User": "Admin",
        "Ideas":[
            {
                "IdeaNum": 1,
                "Revisions":[
                    {
                        "RevNum": 0,
                        "Music": "test.m4a",
                        "Note": "blah blah blah"
                    },
                    {
                        "RevNum": 1,
                        "Music": "demo.mp3",
                        "Note": "yadda yadda yadda"
                    }
                ]
            },
            {
                "IdeaNum": 2,
                "Revisions":[
                    {
                        "RevNum": 0,
                        "Music": "test.m4a",
                        "Note": "blah blah blah"
                    }
                ]
            }
        ]
    }
    ```
