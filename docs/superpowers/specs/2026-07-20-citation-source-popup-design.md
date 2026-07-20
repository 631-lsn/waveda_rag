# Citation Source Popup Design

## Goal

When the user clicks a citation such as `[1]` in an answer, open the matching
original knowledge document in the existing large `SourceViewer` window instead
of rendering it inside the narrow right sidebar.

## Interaction

1. The answer renderer continues to emit `RAGGG_CITATION:<rank>` when a
   citation is clicked.
2. The desktop window resolves the rank only through the current answer's
   `_source_paths` mapping.
3. The matching source is converted to displayable HTML using the existing
   Markdown, HTML, and plain-text handling.
4. A non-modal `SourceViewer` opens at its existing default size of 960×680.
   Its title uses the source document name and it retains the existing close
   button.
5. The main chat window and right sidebar keep their current state.

## Failure Handling

If the citation rank is not present, no window opens. If the mapped file no
longer exists or cannot be read, the existing “source file not found” warning
is shown.

## Verification

- A regression test clicks the citation handling path and checks that
  `SourceViewer` receives the corresponding document HTML.
- The full automated test suite must pass.
- A real Qt WebEngine smoke test clicks a rendered `[1]` and confirms that the
  source viewer becomes visible with the matching document content.
