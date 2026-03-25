# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a single-file browser backgammon game (`backgammon.html`) with a chihuahua theme. There is no build step, no package manager, and no test suite — open the HTML file directly in a browser to run it.

## Development Workflow

- **Run the game:** `open backgammon.html`
- **After any change:** commit and push to GitHub (`jnads/chihuahua-backgammon`)

## Architecture

Everything lives in `backgammon.html` in three sections:

1. **CSS** (`<style>`) — CSS custom properties define the color palette (browns, tans, cream). Board layout uses flexbox. Key variables: `--bd`, `--bm`, `--bl`, `--tan`, `--cream`, `--hi`, `--vm`, `--sel`.

2. **HTML** — Static shell: status bar, dice row, the board (two rows of 12 points + a center bar), home trays, and a game-over modal.

3. **JavaScript** (`<script>`) — All game logic in plain JS, no frameworks.
   - `state` object holds: `board[24]` (positive = human, negative = AI), `bar`, `home`, `dice`, `turn`, `selected`, `phase`
   - `legalMoves(from, die)` — returns valid destination points for a checker given one die value; handles bar entry, hitting blots, and bearing off
   - `applyMove(from, to)` — mutates `state`, handles sending to bar, bearing off
   - `render()` — full re-render from state; builds checker stacks, highlights valid moves in green, dims used dice
   - `aiTurn()` — simple AI: prefers bearing off, then hitting blots, otherwise random legal move; uses `setTimeout` for pacing
   - Bearing-off phase activates when all of a player's checkers are in their home board (points 1–6 for human, 19–24 for AI)

## Git Conventions

- Commit and push after every meaningful change
- Use descriptive commit messages explaining *what changed and why*
- Push to `origin main` after each commit
