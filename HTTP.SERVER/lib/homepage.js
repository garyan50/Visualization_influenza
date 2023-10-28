feather.replace()
view("pastyrs")

function btn_primary_clickable(port, desc) {
  return '<button type="button" class="btn btn-sm btn-primary" onclick="view(\'' + port + '\')">' + desc + '</button>'
}

function btn_secondary_clickable(port, desc) {
  return '<button type="button" class="btn btn-sm btn-secondary" onclick="view(\'' + port + '\')">' + desc + '</button>'
}

function btn_primary_disable(desc) {
  return '<button type="button" class="btn btn-sm btn-primary" disabled>' + desc + '</button>'
}

function btn_secondary_disable(desc) {
  return '<button type="button" class="btn btn-sm btn-secondary" disabled>' + desc + '</button>'
}

function btn_warning(port, desc) {
  return '<button type="button" class="btn btn-sm btn-warning" onclick="view(\'' + port + '\')">' + desc + '</button>'
}

function view(x) {
  $("#showcase").addClass("iframe-placeholder")
  if (x == "wordsRelation") {
    $(".nav-link").removeClass("active")
    $("#" + x + "_label").addClass("active")
    $("#showcase").attr("src", "./wordvec/graphs/2019/influenza.html")
    $("#headline").html(
      '<h4>Word Vector Analysis on Tweets</h4>' +
      '<div class="tipsbar">Click on the stroked nodes to explore more...</div>' +
      btn_warning('wordsRelation', 'Root') +
      '<div class="btn-group" role="group">' +
      btn_secondary_disable('2019') +
      btn_secondary_clickable('relation2020', '2020') + '</div>' +
      '<div class="btn-group" role="group">' +
      btn_primary_disable('Word Neighbours') +
      btn_primary_clickable('effect-1000', 'Effective Size') +
      btn_primary_clickable('proj-1000', 'Word Projection') +
      btn_primary_clickable('sim-1000', 'Word Similarity') + '</div>')
  }
  if (x == "relation2020") {
    $("#showcase").attr("src", "./wordvec/graphs/2020/influenza.html")
    $("#headline").html(
      '<h4>Word Vector Analysis on Tweets</h4>' +
      '<div class="tipsbar">Click on the stroked nodes to explore more...</div>' +
      btn_warning('relation2020', 'Root') +
      '<div class="btn-group" role="group">' +
      btn_secondary_clickable('wordsRelation', '2019') +
      btn_secondary_disable('2020') + '</div>' +
      '<div class="btn-group" role="group">' +
      btn_primary_disable('Word Neighbours') +
      btn_primary_clickable('effect-1000', 'Effective Size') +
      btn_primary_clickable('proj-1000', 'Word Projection') +
      btn_primary_clickable('sim-1000', 'Word Similarity') + '</div>')
  } else if (x == "effect-1000") {
    $("#showcase").attr("src", "./wordvec/Plot_clean_remove_stop/effect-size-10000.html")
    $("#headline").html(
      '<h4>Word Vector Analysis on Tweets</h4>' +
      '<div class="btn-group" role="group">' +
      btn_primary_clickable('wordsRelation', 'Word Neighbours') +
      btn_primary_disable('Effective Size') +
      btn_primary_clickable('proj-1000', 'Word Projection') +
      btn_primary_clickable('sim-1000', 'Word Similarity') + '</div>')
  } else if (x == "proj-1000") {
    $("#showcase").attr("src", "./wordvec/Plot_clean_remove_stop/Projection-10000.html")
    $("#headline").html(
      '<h4>Word Vector Analysis on Tweets</h4>' +
      '<div class="btn-group" role="group">' +
      btn_primary_clickable('wordsRelation', 'Word Neighbours') +
      btn_primary_clickable('effect-1000', 'Effective Size') +
      btn_primary_disable('Word Projection') +
      btn_primary_clickable('sim-1000', 'Word Similarity') + '</div>')
  } else if (x == "sim-1000") {
    $("#showcase").attr("src", "./wordvec/Plot_clean_remove_stop/Sim-influenza-10000.html")
    $("#headline").html(
      '<h4>Word Vector Analysis on Tweets</h4>' +
      '<div class="btn-group" role="group">' +
      btn_primary_clickable('wordsRelation', 'Word Neighbours') +
      btn_primary_clickable('effect-1000', 'Effective Size') +
      btn_primary_clickable('proj-1000', 'Word Projection') +
      btn_primary_disable('Word Similarity') + '</div>')
  } else if (x == "pastyrs") {
    $(".nav-link").removeClass("active")
    $("#" + x + "_label").addClass("active")
    $("#showcase").attr("src", "./nationdata/choropleth.html")
    $("#headline").html("<h4>Influenza-Like Illness (ILI) Activity Level in Past Years</h4>")
  } else if (x == "sent") {
    $(".nav-link").removeClass("active")
    $("#" + x + "_label").addClass("active")
    $("#showcase").attr("src", "./sent/sentiment.html")
    $("#headline").html("<h4>Flu Related Tweet Sentiment Score Since 2019</h4>")
  } else if (x == "pred") {
    $(".nav-link").removeClass("active")
    $("#" + x + "_label").addClass("active")
    $("#showcase").attr("src", "./nationdata/choropleth_pred.html")
    $("#headline").html("<h4>Prediction of ILI Activity Level For Week 41 to Week 52 in 2019</h4>")
  }
}
