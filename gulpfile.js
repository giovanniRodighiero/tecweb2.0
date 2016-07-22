var pug = require('gulp-pug');
var gulp = require('gulp');

gulp.task('xml', function buildHTML() {
  return gulp.src('assets/xml/**/*.pug')
  .pipe(pug({
    pretty: true
    // Your options in here.
  }))
  .pipe(gulp.dest('public_html/xml/'))
});
gulp.task('xsl', function buildHTML() {
  return gulp.src('assets/xsl/**/*.pug')
  .pipe(pug({
    pretty: true
    // Your options in here.
  }))
  .pipe(gulp.dest('public_html/xsl/'))
});

gulp.task('watch', function(){
  gulp.watch('assets/**/*.pug', ['views']);
});

gulp.task('default', ['xml','xsl','watch']);
