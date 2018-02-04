var Metalsmith  = require('metalsmith');
var markdown    = require('metalsmith-markdown');
var layouts     = require('metalsmith-layouts');
var permalinks  = require('metalsmith-permalinks');

Metalsmith(__dirname)
  .metadata({
    title: "Docker 101 for Developers",
    description: "Learn basics of everything You could need with a Docker as a Developer",
    author: "Prakhar Srivastav",
    url: "https://adiq.github.io/docker-101/",
    logo: "https://adiq.github.io/docker-101/images/logo-small.png",
  })
  .source('./src')
  .destination('./public')
  .clean(false)
  .use(markdown())
  .use(permalinks())
  .use(layouts({
    engine: 'handlebars',
    partials: {
      analytics: 'partials/analytics',
      sw: 'partials/sw',
      meta: 'partials/meta',
      styles: 'partials/styles'
    }
  }))
  .build(function(err, files) {
    if (err) { throw err; }
  });
