# Conceptual Mistakes Behind the Bug

This is not about syntax mistakes. These were mostly assumptions about how systems behave.

## 1) Assuming API responses always keep the same shape

You assumed `leaders` would always be a list of leader dictionaries.

Reality: APIs can return different shapes depending on context (expired cookie, rate limit, bad params, server issue). Sometimes you get an error object like `{"message": ...}` instead of a list.

Conceptual correction:
- Treat network/API input as *untrusted data*.
- Validate response shape before iterating (`isinstance(leaders, list)`).
- Fail gracefully when shape is unexpected.

---

## 2) Assuming a one-time check applies inside a loop

You computed `first_bold = par.find("b")` before looping through paragraphs.

Reality: decisions inside a loop must usually be computed from the current loop item. Otherwise you keep reusing stale state.

Conceptual correction:
- Recompute condition values per item when logic depends on each item.
- Keep loop state local to the loop iteration.

---

## 3) Assuming every page follows one exact content pattern

You expected every Wikipedia bio intro to be "first non-empty paragraph with bold" and to always print.

Reality: pages differ. Some have no bold in the expected place, unusual markup, redirects, or language-specific structure.

Conceptual correction:
- Scrapers should have a *primary strategy* and a *fallback strategy*.
- Example: first try bold paragraph; if none, use first non-empty paragraph.

---

## 4) Assuming network calls are reliable enough to ignore failures

The script originally treated `session.get(...)` as always successful.

Reality: timeouts and handshake failures are normal in web scraping.

Conceptual correction:
- Network code should expect occasional failures.
- Catch request exceptions and keep processing next items.
- Prefer partial results over total crash.

---

## 5) Assuming notebook behavior and script behavior are equivalent

In Jupyter, state and execution order can hide brittle assumptions.

Reality: scripts run from a clean start, and timing/environment differences become visible.

Conceptual correction:
- Scripts should be robust from zero state.
- Guard execution with `if __name__ == "__main__":`.
- Avoid relying on hidden notebook state.

---

## 6) Assuming "works on my sample" means "works generally"

The first few leaders/pages can pass, giving confidence.

Reality: edge cases appear later (different countries, different page structure, transient API issues).

Conceptual correction:
- Validate assumptions early with small sanity checks.
- Design loops to continue when one item fails.

---

# Mental Model To Keep

For data collection scripts, think in this order:

1. **External data is variable** (validate shape).
2. **Networks are unreliable** (handle exceptions).
3. **Content formats drift** (fallback extraction strategy).
4. **State can go stale** (compute conditions inside the loop where needed).
5. **Progress beats perfection** (keep going, log failures, return partial results).
