' in current_text:
                current_text = self.text_compressor.minify_code(current_text)
            result["compressed"] = current_text

        # Apply abbreviations if requested
        if use_abbreviations:
            abbreviated_text, used_abbrev = self.abbreviator.abbreviate_text(current_text)
            if used_abbrev:
                header = self.abbreviator.create_abbreviation_header(used_abbrev)
                current_text = f"{header}\n{abbreviated_text}"
                result["abbreviated"] = current_text

        # Apply token optimization if requested
        if optimize_tokens:
            current_text = self.token_optimizer.merge_tokens(current_text)
            current_text = self.token_optimizer.optimize_whitespace(current_text)
            if '