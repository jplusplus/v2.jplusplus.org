#!/usr/bin/coffee
# Encoding: utf-8
# -----------------------------------------------------------------------------
# Project : Journalism++ v2
# -----------------------------------------------------------------------------
# Author : Edouard Richard                                  <edou4rd@gmail.com>
# -----------------------------------------------------------------------------
# License : proprietary journalism++
# -----------------------------------------------------------------------------
# Creation : 24-Apr-2014
# Last mod : 05-May-2014
# -----------------------------------------------------------------------------

class window.Navigation

	constructor: ->
		that = this
		@CONFIG = 
			headerHeight  : 70
			offsetScroll  : 50

		@ui  = $("body > .container-fluid")
		@uis =
			firstPage     : $(".first-page"             , @ui)
			footer        : $(".footer"                 , @ui)
			header        : $(".header"                 , @ui)
			navbar_titles : $(".navbar-menu", ".header" , @ui)
			logo          : $(".navbar-menu .logo", ".header" , @ui)
			titles        : $(".title", ".header"       , @ui)
			body_content  : $("> .body"                 , @ui)
			map           : $(".map"                    , @ui)
			title_flipper : $(".flip-container"         , @ui)
		# set elements size
		@relayout()
		# bind event
		# scrollspy from bootstrap
		$('body').scrollspy({ target: ".navbar-menu", offset: @CONFIG.offsetScroll + @uis.header.offset().top +  @CONFIG.headerHeight })
		# window resize
		lazy_relayout = _.debounce(@relayout, 500)
		$(window).resize(lazy_relayout)
		# listen scroll
		throttled = _.throttle(@onScroll, 100)
		$(window).scroll(throttled)
		@onScroll()
		# when some widgets says that the height has changed (from mosaic for instance)
		$(document).on('heightHasChanged', @relayout)
		# on all anchor links, bind the onTitleClick function and give the #id as parameter
		$("a[href^=#]").on("click", (e) -> e.preventDefault(); that.onTitleClick($(this).attr("href").split("&")[0]))
		# scroll to the anchor if provided in the url
		target = location.hash
		setTimeout((->that.scrollTo(target)), 500) if target
		# hack for z-index
		$(".header .dropdown.languages")
			.on("show.bs.dropdown", => @uis.header.css("z-index", 3))
			.on("hide.bs.dropdown", => @uis.header.css("z-index", 2))
		if @uis.firstPage.length > 0
			@uis.title_flipper.on('click', @onTitleFlipperClick)

	relayout: =>
		that = this
		window_width = $(window).width()
		# map responsive
		@uis.map
			.find(".wrapper")
				# FIXME: hard coded
				.css
					"width"    : window_width
					"height"   : window_width / 3.282051282 # ratio of map picture
					"font-size": "#{Math.min(window_width/1280, 1)}em"
			.find("img")
				.css("width", window_width)
		# set the height of the first page (with the height of the window)
		# in a timeout because window_height should ignore the scrollbar witch can disappear
		if @uis.firstPage.length > 0
			setTimeout(=>
				window_height = $(window).height()
				@uis.firstPage.css
					height: window_height - @uis.body_content.offset().top - @uis.footer.outerHeight(true)
			, 300)
		# center the title links in the header
		if @uis.logo.position().left > 0
			# middle point - (left offset + middle of logo width)
			@uis.navbar_titles.css("left", window_width/2 - (@uis.logo.position().left + @uis.logo.outerWidth(true)/2))
		# refresh scrollspy and show the page if the page was loading
		setTimeout(->
			$("body").each(-> $(this).scrollspy('refresh'))
			that.ui.removeClass("loading")
		, 700) # because of height animation (on first-page for instance)

	onScroll: =>
		scroll_top = $(window).scrollTop()
		# toggle footer
		#  - at top
		if scroll_top == 0
			if @uis.firstPage.length > 0
				@uis.footer.removeClass("light")
		else
			@uis.footer.addClass("light")
		# - at bottom
		if scroll_top >= $(document).height() - $(window).height() then @uis.footer.removeClass("light")
		# toggle header
		if @uis.firstPage.length > 0
			if scroll_top > @CONFIG.headerHeight then @uis.header.removeClass("intro") else @uis.header.addClass("intro")

	scrollTo: (target_id) =>
		offset = $(target_id).offset().top - (@CONFIG.headerHeight + @uis.header.offset().top - @CONFIG.offsetScroll)
		$('html, body').animate({scrollTop: offset}, 'slow')

	onTitleClick: (anchor) =>
		if anchor != "#"
			@scrollTo(anchor)
			# update the url
			window.history.pushState(null, null, anchor);
			return false

	onTitleFlipperClick: (e) =>
		nui = $(e.currentTarget)
		nui.toggleClass("hover")

# EOF
