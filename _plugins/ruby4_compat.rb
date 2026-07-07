# frozen_string_literal: true
#
# LOCAL-ONLY compatibility shim for building this GitHub Pages site on Ruby 3.2+
# (including Ruby 4.0), where the "taint" API was fully removed.
#
# The pinned dependency tree (github-pages -> jekyll 3.9 -> liquid 4.0.3) predates
# that removal and still calls String#untaint from its `escape`/`escape_once`
# filters, plus a few other now-gone stdlib helpers. Without these no-op shims the
# build dies with `undefined method 'untaint' for an instance of String`.
#
# GitHub Pages builds in safe mode and ignores _plugins/, so this file affects
# only local `bundle exec jekyll build|serve` and never runs in production (where
# GitHub's own Ruby 3.3 environment provides a compatible Liquid).

# Restore the removed taint API as harmless no-ops.
module Ruby4TaintCompat
  def taint; self; end
  def untaint; self; end
  def tainted?; false; end
  def trust; self; end
  def untrust; self; end
  def untrusted?; false; end
end
Object.include(Ruby4TaintCompat) unless "".respond_to?(:untaint)

# jekyll 3.9 / its deps occasionally call the long-deprecated *exists? aliases
# that were removed in Ruby 3.2.
File.singleton_class.alias_method(:exists?, :exist?) unless File.respond_to?(:exists?)
Dir.singleton_class.alias_method(:exists?, :exist?) unless Dir.respond_to?(:exists?)
