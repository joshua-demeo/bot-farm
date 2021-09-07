# bot-farm
Bots for tracking specific web events

## Xbox Series X

Built out a web scraper to check for availability of xbox series x on specifc retailer URLs. Logic is contained in `product_availability.py` and exploits specific html elements and attributes in the product webpage to identify whether the given product is available. The script can be passed an email address for which you'd like the message to be sent.

```
python product_availability.py -r example_email@gmail.com
```

This can be scheduled as a re-occuring email via cron. You can add a command like so in your shell:
```
# Open cron editor
crontab -e

# Run script every day at 9:00
0 9 * * * <python executable> <path to product_availability.py> -r <example email>
```
Syntax `<>` are place holders for your local case.

Example for placeholders:
- `<python executable>` -> /Users/jojo/opt/miniconda3/envs/scraper/bin/python
- `<path to product_availability.py>` -> /Users/jojo/bot-farm/xbox-series-x/product_availability.py