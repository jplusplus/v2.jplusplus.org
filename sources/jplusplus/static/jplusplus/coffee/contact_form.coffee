#!/usr/bin/coffee
# Encoding: utf-8
# -----------------------------------------------------------------------------
# Project : Journalism++ v2
# -----------------------------------------------------------------------------
# Author : Edouard Richard                                  <edou4rd@gmail.com>
# -----------------------------------------------------------------------------
# License : proprietary journalism++
# -----------------------------------------------------------------------------
# Creation : 04-May-2014
# Last mod : 04-May-2014
# -----------------------------------------------------------------------------
window.jplusplus = {} if not window.jplusplus

class window.jplusplus.ContactForm


	constructor: (form_ui) ->
		@ui  = $(form_ui)
		@uis =
			submitBtn : $('.nl-submit', @ui)

		new NLForm(@ui.get(0))
		# bind event
		@uis.submitBtn.on("click", @onSubmitClick)

	onSubmitClick: (e) =>
		data = @ui.serialize()
		$.ajax
			url      : @ui.attr("action")
			type     : "post"
			dataType : '"json'
			data     : data
			success  : =>
				console.log "success"
		# prevent the page reload
		e.preventDefault()
		return false


# EOF
