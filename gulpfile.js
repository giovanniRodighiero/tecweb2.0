var pug = require('gulp-pug');
var gulp = require('gulp');
var sass = require('gulp-sass');
var concat = require('gulp-concat');
var ext_replace = require('gulp-ext-replace');

gulp.task('xml', function buildHTML() {
  return gulp.src('assets/xml/**/*.pug')
  .pipe(pug({
    pretty: true,
    doctype: 'xml'
    // Your options in here.
  }))
  .pipe(ext_replace('.xml'))
  .pipe(gulp.dest('public_html/xml/'))
});
gulp.task('xsl', function buildHTML() {
  return gulp.src('assets/xsl/**/*.pug')
  .pipe(pug({
    pretty: true
    // Your options in here.
  }))
  .pipe(ext_replace('.xsl'))
  .pipe(gulp.dest('public_html/xsl/'))
});
gulp.task('defaultStyle', () => {
  return gulp.src('assets/style/default/**/*.sass')
  .pipe(sass({outputStyle: 'compressed'}).on('error', sass.logError))
  .pipe(concat('main.min.css'))
  .pipe(gulp.dest('public_html/styles/'));
});
gulp.task('printStyle', () => {
  return gulp.src('assets/style/print/**/*.sass')
  .pipe(sass({outputStyle: 'compressed'}).on('error', sass.logError))
  .pipe(concat('print.min.css'))
  .pipe(gulp.dest('public_html/styles/'));
})
gulp.task('watch', function(){
  gulp.watch('assets/xml/**/*.pug', ['xml']);
  gulp.watch('assets/xsl/**/*.pug', ['xsl']);
  gulp.watch('assets/style/default/**/*.sass', ['defaultStyle']);
  gulp.watch('assets/style/print/**/*.sass', ['printStyle']);
});

gulp.task('default', ['xml','xsl','defaultStyle','printStyle','watch']);
