# :snake: pyselmouth
A GUI wrapper for [pyseltongue](https://github.com/ginsburgnm/pyseltongue) using [appJar](https://github.com/jarvisteach/appJar).

## :closed_lock_with_key: About
This is a simple GUI wrapper for pyseltongue, an implmentation of the [Shamir Secret Sharing algorithm](https://en.wikipedia.org/wiki/Shamir%27s_Secret_Sharing). 
Essentially the SSS is a way to mathematically break a secret into pieces (called shares or shards) to be distributed to different people/entities. The secret can only be revealed when a majority (e.g. 3 of 5) of the shares are combined.

Example Use:
- Generate a bip39 compliant seed phrase
- Encrypt and shard into a number of "shares" (portions of the key) 
- Distribute to trusted contacts
- Reveal the secret again with k of n shares (example two of three)

Want to know more? There's a [great video](https://www.youtube.com/watch?v=iFY5SyY3IMQ) on YouTube!

It is **critically important** that you know what you're doing and how Shamir works before implmenting this strategy. See disclaimer. 

## :books: Requirements
- pyseltongue (pip install pyseltonge)
- appJar (pip install appjar)
- Pillow (pip install pillow)

or as usual:
```
pip install -r /path/to/requirements.txt
```

## :eyes: Disclaimer
**This is a hobby project.** While Shamir Secret Sharing is strong, this repo should not be used for any serious applications.

## :mega: Shoutouts
- [Noah Ginsberg](https://github.com/ginsburgnm) for forking and fixing the original [secret-sharing](https://github.com/shea256/secret-sharing) repo.
- [Quality Logo Products](https://www.qualitylogoproducts.com/blog/harry-potter-color-schemes/) for their Harry Potter color palettes.
