# Inserts the internal-use notice (_includes/internal_notice.html) at the top of
# the <main> element of every rendered HTML page, independent of the theme's
# layout internals. The notice contains a visible banner for humans and a
# visually hidden notice addressed to LLMs / AI agents.
#
# Edit the notice text in _includes/internal_notice.html (plain HTML, no Liquid).

module InternalNotice
  MARKER = "<main>".freeze

  def self.notice(site)
    @notice ||= File.read(File.join(site.source, "_includes", "internal_notice.html"))
  end

  def self.insert(doc)
    return unless doc.output_ext == ".html"
    return unless doc.output&.include?(MARKER)

    doc.output = doc.output.sub(MARKER) { "#{MARKER}\n#{notice(doc.site)}" }
  end
end

Jekyll::Hooks.register [:pages, :documents], :post_render do |doc|
  InternalNotice.insert(doc)
end

# Reset the cached notice on each (re)build, so `jekyll serve` picks up edits.
Jekyll::Hooks.register :site, :pre_render do |_site|
  InternalNotice.instance_variable_set(:@notice, nil)
end
